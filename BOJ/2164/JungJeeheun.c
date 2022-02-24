#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

struct NODE //구조체 선언
{
    struct NODE* llink;
    int data;
    struct NODE* rlink;
};
struct NODE* head;
struct NODE* tail;

//노드 생성 함수
struct NODE* makenode(int value) {
    struct NODE* node = (struct NODE*)malloc(sizeof(struct NODE));
    node->llink = NULL;
    node->data = value;
    node->rlink = NULL;
    return node;
}

//출력 함수
void print() {
    struct NODE* p;
    p = head->rlink;
    while (p->rlink != tail) {
        printf("%d", p->data);
        p = p->rlink;
    }
    printf("%d", p->data);
}

//초기화 함수
void init() {
    head = (struct NODE*)malloc(sizeof(struct NODE));
    tail = (struct NODE*)malloc(sizeof(struct NODE));
    head->data = 0;
    tail->data = 0;

    head->rlink = tail;
    head->llink = head;
    tail->rlink = tail;
    tail->llink = head;
}

//뒤로부터 노드 추가하는 함수
void push_back(int value) {
    struct NODE* newnode = makenode(value);
    struct NODE* p;
    p = tail;
    p->llink->rlink = newnode;
    newnode->llink = p->llink;
    p->llink = newnode;
    newnode->rlink = p;
}

void removenode() {
    struct NODE* p;
    p = head->rlink;
    p->rlink->llink = p->llink;
    p->llink->rlink = p->rlink;
    free(p);
}
//main함수
int main() {
    int N;
    scanf("%d", &N);
    init(); //head와 tail 초기화 (data = 0)
    for(int i = 1; i <= N; i++)
        push_back(i);
    while (1) {
        if (head->rlink->rlink == tail)
            break;
        removenode();
        if (head->rlink->rlink == tail)
            break;
        push_back(head->rlink->data);
        removenode();
    }
    print();  //출력
    return 0;
}
