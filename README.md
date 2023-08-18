# pico-fireclock-on-16x10LED

![ezgif com-video-to-gif](https://github.com/nosferathoo/pico-fireclock-on-16x10LED/assets/2834098/1d64f51b-5a88-434d-b74f-35be0019b92d)

![IMG_4101](https://github.com/nosferathoo/pico-fireclock-on-16x10LED/assets/2834098/3519edfc-a165-44e5-ad9c-471f70f85679) ![IMG_4109](https://github.com/nosferathoo/pico-fireclock-on-16x10LED/assets/2834098/8bc2aa30-f4a6-4396-8012-2c4ac6da1527)

Simple clock with procedural fire effect displayed on 16x10 RGB LED Grid using Micropython on Raspberry Pi Pico.

RTC is not needed because time can be set on startup using BOOTSEL button (click to change blinking digit, hold to skip to next digit/end setup).

During normal mode BOOTSEL button cycles brightness.

For case I used 3D printed model from [my previous project](https://github.com/nosferathoo/pico-raw-video-on-16x10LED)

## Requirements

* Raspberry Pi Pico
* 16x10 RGB LCD Grid (like [this](https://botland.com.pl/raspberry-pi-pico-hat-klawiatury-i-wyswietlacze/20116-matryca-led-rgb-16x10-do-raspberry-pi-pico-waveshare-20170-5904422350666.html))

## Installation

Use for example Thonny IDE to install MicroPython env and upload both python files.
