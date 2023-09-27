int led_pin1 = 13;
int led_pin2 = 12;
int blink_duration1 = 500;


void setup() {

}

void loop() {
  
digitalWrite (13,HIGH);
delay (blink_duration1);
digitalWrite (13,LOW);
delay (blink_duration1);

digitalWrite (12,HIGH);
delay (blink_duration1);
digitalWrite (12,LOW);
delay (blink_duration1);

}
