#include <stdio.h>
#include "dut.h"

//argc is counting the items typed into terminal
//argv is the array of string that holds the text of those items
//when typing "./simulator ARMED_DOOR_OPEN" into terminal, argv[0] = ./simulator and argv[1] = ARMED_DOOR_OPEN
int main(int argc, char *argv[]){
    if (argc <2){
        printf("ERROR_NO_INPUT\n");
        return 1;
    }
    //declare output response
    char response[MAX_MSG_LEN];
    //when calling no need to write char and input output
    eval_alarm_state(argv[1], response);
    printf("%s\n", response);
    return 0;
}
