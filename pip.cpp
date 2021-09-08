#define ledPin 13 // choose the pin for the LED
#define switchPin 7 // choose the input pin (for a pushbutton)

int val = 0; // variable for reading the pin status

void setup()
{
  pinMode(ledPin, OUTPUT); // declare LED as output
  pinMode(switchPin, INPUT); // declare pushbutton as input
}

void loop()
{
  val = digitalRead(switchPin); // read input value
  if (val == HIGH)
  { // check if the input is HIGH (button released)
    digitalWrite(ledPin, LOW); // turn LED OFF
  } else {
    digitalWrite(ledPin, HIGH); // turn LED ON } }
  }
}