#ifndef OS_COMMAND_H
#define OS_COMMAND_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/stat.h>

#ifdef _WIN32
#include <direct.h> // Windows 下的目录操作
#define GetCurrentDir _getcwd
#else
#include <unistd.h> // Unix/Linux 下的目录操作
#define GetCurrentDir getcwd
#endif

// 结构体定义
typedef struct {
    char time[64];
    char command[256];
    char* stdout_output;
    char* stderr_output;
    int return_code;
} CommandHistoryEntry;

// 全局变量
extern CommandHistoryEntry* history;
extern int history_count;
extern int history_capacity;
extern char working_directory[256];

// 函数声明
void init_executor(const char* initial_directory);
void set_working_directory(const char* directory);
void execute_command(const char* command, int capture_output, int print_output);
void get_command_history();
void save_history_to_file(const char* filename);
void cleanup();

#endif // OS_COMMAND_H