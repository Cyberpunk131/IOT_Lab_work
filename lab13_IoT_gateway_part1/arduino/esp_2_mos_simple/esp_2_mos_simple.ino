void setup() {
  Serial.begin(115200);
  Serial.println("Simple Serial Test"); // This should print
}
void loop() {
  delay(1000);
  Serial.println("Looping...");
}
