# Monitor Control

Gigabyte G27Q monitor control application, now with a CLI interface for scripting and automation

## Usage
The program is called as a python module. use
```
pip -m monctl gui
```
to access the original monctl GUI, or use
```
pip -m monctl cli <arguments>
```
to access the new CLI. Convenience scripts are provided in resources for monctl and moncli, which automatically pass your arguments through to moncli.

### moncli arguments

```
kalium@cinnabar : ~/code/monctl
[0] » sh resources/moncli -h  
usage: moncli [-h] [-b BRIGHTNESS] [-c CONTRAST] [-s SHARPNESS]
              [-w BLUELIGHT] [-r] [-p]

Command line add-on to monctl by Gothem, a Gigabyte monitor control program

options:
  -h, --help            show this help message and exit
  -b BRIGHTNESS, --brightness BRIGHTNESS
                        brightness [1-100]
  -c CONTRAST, --contrast CONTRAST
                        contrast [1-10]0
  -s SHARPNESS, --sharpness SHARPNESS
                        sharpness [1-10]
  -w BLUELIGHT, --bluelight BLUELIGHT
                        display warmth [1-10]
  -r, --relative        change value(s) relatively instead of absolutely
  -p, --print           print current values

see https://github.com/KaliumPuceon/monctl for some more details especially
if you want to try scripting with this
```

## Installation

### pip
Distribution still being worked out

```
git clone 'https://github.com/KaliumPuceon/monctl'
pip install monctl
```



