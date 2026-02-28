#include "os_command.h"

// win : gcc -shared -fPIC -o os_command.dll os_command.c


// 全局变量定义
CommandHistoryEntry* history = NULL;
int history_count = 0;
int history_capacity = 0;
char working_directory[256] = {0};

// 获取当前时间字符串
void get_current_time(char* buffer, size_t size) {
    time_t raw_time;
    struct tm* time_info;

    time(&raw_time);
    time_info = localtime(&raw_time);
    strftime(buffer, size, "%Y-%m-%d %H:%M:%S", time_info);
}

// 初始化执行器
void init_executor(const char* initial_directory) {
    if (initial_directory && strlen(initial_directory) > 0) {
        strncpy(working_directory, initial_directory, sizeof(working_directory) - 1);
    } else {
        GetCurrentDir(working_directory, sizeof(working_directory));
    }
}

// 设置工作目录
void set_working_directory(const char* directory) {
    struct stat info;
    if (stat(directory, &info) == 0 && S_ISDIR(info.st_mode)) {
        strncpy(working_directory, directory, sizeof(working_directory) - 1);
        printf("工作目录已切换至: %s\n", working_directory);
    } else {
        fprintf(stderr, "无效的目录路径: %s\n", directory);
        exit(EXIT_FAILURE);
    }
}

// 执行命令
void execute_command(const char* command, int capture_output, int print_output) {
    char full_command[512];
    snprintf(full_command, sizeof(full_command), "cd %s && %s", working_directory, command);

    FILE* pipe = popen(full_command, "r");
    if (!pipe) {
        perror("执行命令失败");
        exit(EXIT_FAILURE);
    }

    char buffer[4096];
    char* stdout_output = malloc(1); *stdout_output = '\0';
    char* stderr_output = malloc(1); *stderr_output = '\0';

    while (fgets(buffer, sizeof(buffer), pipe)) {
        if (capture_output) {
            char* temp = realloc(stdout_output, strlen(stdout_output) + strlen(buffer) + 1);
            if (temp) {
                stdout_output = temp;
                strcat(stdout_output, buffer);
            }
        }
        if (print_output) {
            printf("%s", buffer);
        }
    }

    int return_code = pclose(pipe);

    CommandHistoryEntry entry;
    get_current_time(entry.time, sizeof(entry.time));
    strncpy(entry.command, command, sizeof(entry.command) - 1);
    entry.stdout_output = stdout_output;
    entry.stderr_output = stderr_output;
    entry.return_code = return_code;

    if (history_count >= history_capacity) {
        history_capacity += 10;
        history = realloc(history, history_capacity * sizeof(CommandHistoryEntry));
    }
    history[history_count++] = entry;
}

// 获取命令历史
void get_command_history() {
    for (int i = 0; i < history_count; ++i) {
        printf("[%s] %s\n", history[i].time, history[i].command);
        printf("STDOUT:\n%s\n", history[i].stdout_output);
        printf("STDERR:\n%s\n", history[i].stderr_output);
        printf("Return Code: %d\n\n", history[i].return_code);
    }
}

// 保存历史到文件
void save_history_to_file(const char* filename) {
    FILE* file = fopen(filename, "w");
    if (!file) {
        perror("打开文件失败");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < history_count; ++i) {
        fprintf(file, "[%s] %s\n", history[i].time, history[i].command);
        fprintf(file, "STDOUT:\n%s\n", history[i].stdout_output);
        fprintf(file, "STDERR:\n%s\n", history[i].stderr_output);
        fprintf(file, "Return Code: %d\n\n", history[i].return_code);
    }

    fclose(file);
    printf("历史记录已保存至: %s\n", filename);
}

// 清理资源
void cleanup() {
    for (int i = 0; i < history_count; ++i) {
        free(history[i].stdout_output);
        free(history[i].stderr_output);
    }
    free(history);
    history = NULL;
    history_count = 0;
    history_capacity = 0;
}