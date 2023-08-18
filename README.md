# pico-fireclock-on-16x10LED

![ezgif com-optimize](https://github.com/nosferathoo/pico-fireclock-on-16x10LED/assets/2834098/f90afb6f-abbf-42b1-8463-ec4b79b0dca0)

Simple clock with procedural fire effect displayed on 16x10 RGB LED Grid using Micropython on Raspberry Pi Pico.

RTC is not needed because time can be set on startup using BOOTSEL button (click to change blinking digit, hold to skip to next digit/end setup).

During normal mode BOOTSEL button cycles brightness.

For case I used 3D printed model from [my previous project](https://github.com/nosferathoo/pico-raw-video-on-16x10LED)

## Requirements

* Raspberry Pi Pico
* 16x10 RGB LCD Grid (like [this](https://botland.com.pl/raspberry-pi-pico-hat-klawiatury-i-wyswietlacze/20116-matryca-led-rgb-16x10-do-raspberry-pi-pico-waveshare-20170-5904422350666.html))

## Installation

Use for example Thonny IDE to install MicroPython env and upload both python files.
