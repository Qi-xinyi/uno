#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define M 50
typedef struct
{
    char name[20];
    char units[30];
    char tele[10];
} ADDRESS;

void gotoxy_ansi(int x, int y)
{
    printf("\033[%d;%dH", y, x);
}

int in_it(ADDRESS adr[], char *target, int n);
void addimportant(ADDRESS t[], int n);
int enter(ADDRESS t[], int length);
void list(ADDRESS t[], int n);
void search(ADDRESS t[], int n);
int delete(ADDRESS t[], int n);
int add(ADDRESS t[], int n);
void save(ADDRESS t[], int n);
int load(ADDRESS t[]);
void display(ADDRESS t[]);
void sort(ADDRESS t[], int n);
void qseek(ADDRESS t[], int n);
void copy();
void print(ADDRESS temp);
int menu_select();
int check(ADDRESS t[], int length);

int main()
{
    int length = 0;
    int i;
    ADDRESS adr[M];
    system("cls");
    for (;;)
    {
        length = length - check(adr, length);
        switch (menu_select())
        {
        case 0:
            length = enter(adr, length);
            break;
        case 1:
            list(adr, length);
            break;
        case 2:
            search(adr, length);
            break;
        case 12:
            search_(adr, length);
            break;
        case 13:
            addimportant(adr, length);
            break;
        case 3:
            length = delete (adr, length);
            break;
        case 4:
            length = add(adr, length);
            break;
        case 5:
            save(adr, length);
            break;
        case 6:
            length = load(adr);
            break;
        case 7:
            display(adr);
            break;
        case 8:
            sort(adr, length);
            break;
        case 9:
            qseek(adr, length);
            break;
        case 10:
            copy();
            break;
        case 11:
            exit(0);
        }
    }
}

int check(ADDRESS t[], int length)
{
    int i, j, k, remove = 0;
    for (i = 0; i < length - 1; i++)
    {
        for (j = i + 1; j < length; j++)
        {
            if (!strcmp(t[i].name, t[j].name))
            {
                print(t[j]);
                printf("the record is repeated\n");
                remove++;
                for (k = j; k < length - 1; k++)
                {
                    t[k] = t[k + 1];
                }
                j--;
                length--;
                i--;
                printf("I have deleted the record");
                getchar();
                getchar();
                getchar();
            }
        }
    }
    return remove;
}

int menu_select()
{
    char s[80];
    int c;
    gotoxy_ansi(1, 25);
    printf("press any key entre mrnu");
    system("cls");
    gotoxy_ansi(1, 1);
    printf("******************MENU******************\n");
    printf("\t0.Enter record\n");
    printf("\t1.List the file\n");
    printf("\t*.list the important record\n");
    printf("\tadd*.add the important record\n");
    printf("\t2.Search record on name\n");
    printf("\t3.Delete a record\n");
    printf("\t4.add record\n");
    printf("\t5.Save the file\n");
    printf("\t6.Load the file\n");
    printf("\t7.display the file\n");
    printf("\t8.sort to make new file\n");
    printf("\t9.Quick seek record\n");
    printf("\t10.copy the file to new file\n");
    printf("\t11.Quit\n");
    printf("****************************************");
    do
    {
        printf("\n Enter your choice(0~11 or * or add*):");
        scanf("%s", s);
        if (strcmp(s, "*") == 0)
            strcpy(s, "12");
        if (strcmp(s, "add*") == 0)
            strcpy(s, "13");
        c = atoi(s);
    } while (c < 0 || c > 13);
    return c;
}

int enter(ADDRESS t[], int length)
{
    int i, n;
    char *s;
    system("cls");
    printf("\nPlease input the number of the record that you want to input\n");
    scanf("%d", &n);
    printf("Please input the record \n");

    printf("        name                       unit                  telephone\n");
    printf("------------------------------------------------------------------\n");
    for (i = 0; i < n; i++)
    {
        scanf("%s%s%s", t[length + i].name, t[length + i].units, t[length + i].tele);
        printf("------------------------------------------------------------------\n");
    }
    return n + length;
}

void list(ADDRESS t[], int n)
{
    int i;
    system("cls");
    printf("\n\n****************************ADDRESS*******************************\n");
    printf("        name                       unit                  telephone\n");
    printf("------------------------------------------------------------------\n");
    for (i = 0; i < n; i++)
        printf("%-20s%-30s%-10s\n", t[i].name, t[i].units, t[i].tele);
    if ((i + 1) % 10 == 0)
    {
        printf("Press any key continue...\n");
    }
    printf("****************************end**********************************\n");
    getchar();
    getchar();
    getchar();
}

void search_(ADDRESS t[], int n)
{
    char s[20];
    int i;
    int a = 0;
    system("cls");
    printf("\n\n****************************ADDRESS*******************************\n");
    printf("        name                       unit                  telephone\n");
    for (i = 0; i < n; i++)
    {
        if (t[i].name[0] == '*')
            printf("%-20s%-30s%-10s\n", t[i].name, t[i].units, t[i].tele);
        a++;
    }
    if (a == 0)
        printf("Not found\n");
    printf("****************************end**********************************\n");
    getchar();
    getchar();
    getchar();
}

void search(ADDRESS t[], int n)
{
    char s[20];
    int i;

    system("cls");
    printf("Please input the name you want to search\n");
    scanf("%s", s);
    i = find(t, n, s);
    if (i > n - 1)
    {
        printf("Not found\n");
        getchar();
        getchar();
        getchar();
    }
    else
        print(t[i]);
}

void print(ADDRESS temp)
{
    system("cls");
    printf("\n\n*************************************\n");
    printf("        name                       unit                  telephone\n");
    printf("------------------------------------------\n");
    printf("%-20s%-30s%-10s\n", temp.name, temp.units, temp.tele);
    printf("******************end*******************\n");
    getchar();
    getchar();
    getchar();
}

int find(ADDRESS t[], int n, char s[])
{
    int i;
    for (i = 0; i < n; i++)
    {
        if (strcmp(s, t[i].name) == 0)
            return i;
    }
    return i;
}

int delete(ADDRESS t[], int n)
{
    char s[20]; // 要删除记录的姓名
    int ch = 0;
    int i, j;
    printf("please deleted name:\n"); // 提示信息
    scanf("%s", s);                   // 输入姓名
    i = find(t, n, s);                // 调用find函数查找姓名
    if (i > n - 1)
    {                                    // 如果未找到（索引超出范围）
        printf("no found not delete\n"); // 显示未找到
    }
    else
    {
        print(t[i]);                             // 调用输出函数显示该条记录信息
        printf("Are you sure delete if(1/0)\n"); // 确认是否要删除
        scanf("%d", &ch);                        // 输入确认信息
        if (ch == 1)
        { // 如果确认删除
            for (j = i + 1; j < n; j++)
            { // 从当前位置开始，后续记录前移
                strcpy(t[j - 1].name, t[j].name);
                strcpy(t[j - 1].units, t[j].units);
                strcpy(t[j - 1].tele, t[j].tele);
            }
            n--; // 记录数减1
        }
    }
    getchar();
    getchar();
    getchar();
    return n; // 返回更新后的记录数
}

int add(ADDRESS t[], int n) /* 插入函数，参数为结构体数组和记录数 */
{
    ADDRESS temp; /* 新插入记录信息 */
    int i, j;
    char s[20]; /* 确定插入在哪个记录之前（此变量在后续代码中未直接使用，可能是用于输入或逻辑判断）*/
    printf("please input record\n");
    printf("**********************************\n");
    printf("name\tunit\ttelephone\n");
    printf("------------------------------------------\n");
    scanf("%s%s%s", temp.name, temp.units, temp.tele);
    printf("-------------------------------------------\n");
    printf("please input locate name \n");
    scanf("%s", s);              /*输入插入位置的姓名*/
    i = find(t, n, s);           /*调用find,确定插入位置*/
    for (j = n - 1; j >= i; j--) /*从最后一个结点开始向后移动一条*/
    {
        strcpy(t[j + 1].name, t[j].name);
        strcpy(t[j + 1].units, t[j].units);
        strcpy(t[j + 1].tele, t[j].tele);
    }
    strcpy(t[i].name, temp.name); /*将新插入记录拷贝到第i个位置*/
    strcpy(t[i].units, temp.units);
    strcpy(t[i].tele, temp.tele);
    n++; /*记录数加1*/
    getchar();
    getchar();
    getchar();
    return n; /*返回记录数*/
}

/*保存函数，参数为结构体数组和记录数*/
void save(ADDRESS t[], int n)
{
    int i;
    FILE *fp; /*指向文件的指针*/
    if ((fp = fopen("record.txt", "wb")) == NULL)
    {
        printf("can not open file\n"); /*不能打开文件*/
        exit(1);                       /*退出*/
    }
    printf("\nSaving file\n"); /*输出提示信息*/
    fprintf(fp, "%d", n);      /*将记录数写入文件*/
    fprintf(fp, "\n");         /*将换行符号写入文件*/
    fprintf(fp, "name unit telephone\n");
    for (i = 0; i < n; i++)
    {
        fprintf(fp, "%s %s %s", t[i].name, t[i].units, t[i].tele); /*格式写入记录*/
        fprintf(fp, "\n");                                         /*将换行符号写入文件*/
    }
    fclose(fp);               /*关闭文件*/
    printf("save success\n"); /*显示保存成功*/
    getchar();
    getchar();
    getchar();
}

/*读入函数，参数为结构体数组*/
int load(ADDRESS t[])
{
    char s[1024];
    int i, n;
    FILE *fp;                                     /*指向文件的指针*/
    if ((fp = fopen("record.txt", "rb")) == NULL) /*打开文件*/
    {
        printf("can not open file\n"); /*不能打开*/
        exit(1);                       /*退出*/
    }
    fscanf(fp, "%d", &n); /*读入记录数*/
    fgets(s, sizeof(s), fp);
    fgets(s, sizeof(s), fp);
    for (i = 0; i < n; i++)
        fscanf(fp, "%s %s %s", t[i].name, t[i].units, t[i].tele); /*按格式读入记录*/
    fclose(fp);                                                   /*关闭文件*/
    printf("You have success read data from file!!!\n");          /*显示保存成功*/
    getchar();
    getchar();
    getchar();
    return n; /*返回记录数*/
}

/*按序号显示记录函数*/
void display(ADDRESS t[])
{
    int id, n;
    char k[1024];
    FILE *fp;
    if ((fp = fopen("record.txt", "rb")) == NULL)
    {
        printf("Cannot open file\n");
        exit(1);
    }
    printf("Enter order number...\n");
    scanf("%d", &id);
    id = id - 1;
    fscanf(fp, "%d", &n);

    if (id >= 0 && id < n)
    {
        fseek(fp, (id - 1) * (sizeof(ADDRESS) + 1), 1);

        print(t[id]);

        printf("\n");
    }
    else
    {
        printf("No %d number record!\n", id);
    }

    fclose(fp);
}

/*排序函数，参数为结构体数组和记录数*/
void sort(ADDRESS t[], int n)
{
    int i, j, flag;
    ADDRESS temp;               /*临时变量做交换数据用*/
    for (i = 0; i < n - 1; i++) /*注意这里调整为n-1，因为冒泡排序最后一轮无需再比较*/
    {
        flag = 0;                                     /*设标志，判断是否发生过交换*/
        for (j = 0; j < n - 1 - i; j++)               /*减少内层循环次数，提高效率*/
            if (strcmp(t[j].name, t[j + 1].name) > 0) /*比较大小*/
            {
                flag = 1;
                strcpy(temp.name, t[j].name); /*交换记录*/
                strcpy(temp.units, t[j].units);
                strcpy(temp.tele, t[j].tele);
                strcpy(t[j].name, t[j + 1].name);
                strcpy(t[j].units, t[j + 1].units);
                strcpy(t[j].tele, t[j + 1].tele);
                strcpy(t[j + 1].name, temp.name);
                strcpy(t[j + 1].units, temp.units);
                strcpy(t[j + 1].tele, temp.tele);
            }
        if (flag == 0)
            break; /*如果标志为0，说明没有发生过交换，循环结束*/
    }
    printf("sort success!!!\n"); /*显示排序成功*/
}

/*快速查找，参数为结构体数组和记录数*/
void qseek(ADDRESS t[], int n)
{
    char s[20];
    int l, r, m;
    printf("\nPlease sort before qseek!\n"); /*提示确认在查找之前，记录是否已排序*/
    printf("please enter name for qseek\n"); /*提示输入*/
    scanf("%s", s);                          /*输入待查找的姓名*/
    l = 0;
    r = n - 1;     /*设置左边界与右边界的初值*/
    while (l <= r) /*当左边界<=右边界时*/
    {
        m = (l + r) / 2;               /*计算中间位置*/
        if (strcmp(t[m].name, s) == 0) /*与中间结点的姓名字段进行比较，判断是否相等*/
        {
            print(t[m]); /*如果相等，则输出找到的姓名*/
            return;      /*返回*/
        }
        if (strcmp(t[m].name, s) < 0) /*如果中间结点小*/
            l = m + 1;                /*修改左边界*/
        else
            r = m - 1; /*否则，中间结点大，修改右边界*/
    }
    if (l > r)                 /*如果左边界大于右边界时*/
        printf("not found\n"); /*显示没找到*/
}


void copy()
{
    char outfile[20]; /*目标文件名*/
    int i, n;
    ADDRESS temp[M];                               /*定义临时变量，注意M应为已定义的常量或变量*/
    FILE *sfp, *tfp;                               /* 定义指向文件的指针 */
    system("cls");                                 /* 清屏 */
    if ((sfp = fopen("record.txt", "rb")) == NULL) /* 打开记录文件 */
    {
        printf("can not open file\n"); /* 显示不能打开文件的信息 */
        exit(1);                       /* 退出 */
    }
    printf("Enter outfile name, for example c:\\fl\\te.txt:\n"); /* 提示信息 */
    scanf("%s", outfile);                                        /* 输入目标文件名 */
    if ((tfp = fopen(outfile, "wb")) == NULL)                    /* 打开目标文件 */
    {
        printf("can not open file\n"); /* 显示不能打开文件的信息 */
        exit(1);                       /* 退出 */
    }
    fscanf(sfp, "%d", &n); /* 读出文件记录数 */
    fprintf(tfp, "%d", n); /* 写入目标文件数 */
    fprintf(tfp, "\r\n");    /* 写入换行符 */
    for (i = 0; i < n + 1; i++)
    {
        fscanf(sfp, "%s %s %s\n", temp[i].name, temp[i].units, temp[i].tele);  /* 读入记录 */
        fprintf(tfp, "%s %s %s\n", temp[i].name, temp[i].units, temp[i].tele); /* 写入记录 */
        fprintf(tfp, "\n");                                                    /* 写入换行符 */
    }
    fclose(sfp);                               /* 关闭源文件 */
    fclose(tfp);                               /* 关闭目标文件 */
    printf("you have success.copy file!!!\n"); /* 显示复制成功 */
}

int in_it(ADDRESS adr[], char *target, int n)
{
    for (int i = 0; i < n; i++)
        if (strcmp(adr[i].name, target) == 0)
            return i;
    return -1;
}

void addimportant(ADDRESS adr[], int length)
{
    int i = 0;
    char a[30];
    char t[33]="* ";
    printf("enter name: ");
    scanf("%s", a);
    if (in_it(adr, a, length) != -1)
    {
        i = in_it(adr, a, length);
        strcpy(adr[i].name, strcat(t, a));
    }
    else
        printf("not found\n");
    getchar();
    getchar();
    getchar();
}