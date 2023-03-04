#include <WiFi.h>
#include <WiFiUDP.h>

const char* ssid = "IZV";
const char* password = "@skola12";

WiFiUDP UDP;

unsigned int localUDPPort = 34623;  // local port to listen on
char incoming[255];  // buffer for incoming packets
char reply[] = "Hi there! Got the message :-)";  // a reply string to send back


void setup()
{
  Serial.begin(115200);
  Serial.println();
  delay(2000);
  Serial.printf("Connecting to %s ", ssid);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println(" connected");

  UDP.begin(localUDPPort);
  Serial.printf("Now listening at IP %s, UDP port %d\n", WiFi.localIP().toString().c_str(), localUDPPort);
}

void loop()
{
  // send back a reply, to the IP address and port we got the packet from
  UDP.beginPacket("10.109.6.206", 35682);
  UDP.print(reply);
  UDP.endPacket();
  UDP.parsePacket();
  if()
  delay(2000);
}
