#include "dut.h"
#include <string.h>

void eval_alarm_state(const char input[], char output[]){

  //evaluate know sensor states
  if (strncmp(input, "ARMED_DOOR_OPEN", MAX_MSG_LEN) == 0){
    strncpy(output, "TRIGGER_ALARM", MAX_MSG_LEN);
  }
  else if (strncmp(input, "ARMED_MOTION", MAX_MSG_LEN) ==0){
    strncpy(output,"TRIGGER_ALARM",MAX_MSG_LEN);
  }
  else if (strncmp(input, "DISARMED_DOOR_OPEN", MAX_MSG_LEN) ==0){
    strncpy(output, "SYSTEM_SAFE", MAX_MSG_LEN);
  }
  //for invalid data
  else{
    strncpy(output, "SAFE_STATE_ERROR", MAX_MSG_LEN);
  }
  output[MAX_MSG_LEN - 1]= '\0';
}