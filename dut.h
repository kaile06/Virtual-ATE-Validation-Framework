#ifndef DUT_H //checks if file is read
#define DUT_H

//define max length for safe state 
#define MAX_MSG_LEN 32

//evaluate sensor inputs
void eval_alarm_state(const char input[], char output[]); //const means read only

#endif //reading stopping point