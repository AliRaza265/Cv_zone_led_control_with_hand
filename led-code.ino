#include<cvzone.h>

SerialData serial_data(1,1);

int arr[1];
int pin_no = 3;

void setup(){
    serial_data.begin();
    pinMode(pin_no,OUTPUT);
}
void loop(){
  serial_data.Get(arr);
  digitalWrite(pin_no,arr[0]);
}