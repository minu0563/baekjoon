#include <stdio.h>
#include <string.h>

void removeDuplicates(char* str) {
    int index = 0;
    char result[128] = { 0 };  // 결과 문자열을 저장할 배열
    char lastChar = '\0';     // 마지막으로 출력된 문자

    // 문자열을 순차적으로 처리
    for (int i = 0; str[i] != '\0'; i++) {
        if (str[i] != lastChar) {  // 연속된 문자가 아니면
            result[index++] = str[i];  // 결과 배열에 추가
            lastChar = str[i];          // 마지막 문자 업데이트
        }
    }

    result[index] = '\0';  // 문자열 종료
    printf("%s\n", result);  // 결과 출력
}

int main() {
    int T;  // 테스트 케이스 수
    scanf("%d", &T);  // 테스트 케이스 수 입력받기

    for (int t = 0; t < T; t++) {
        char str[100];  // 각 테스트 케이스의 문자열

        scanf("%s", str);  // 문자열 입력받기

        removeDuplicates(str);  // 중복 제거 함수 호출
    }

    return 0;
}
