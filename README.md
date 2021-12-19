# colorswap

This is a simple image processing script. It extracts palette from an image by iterating over pixels. You can change this palette and based on the changed palette script can update original image. Nothing sophisticated but fun to play and bring some new life in the old games. If you like it please consider leaving a heart [here](https://twitter.com/MarekNarozniak/status/1472225450038476801) and [giving me a follow](https://twitter.com/MarekNarozniak). Senks!

## Setup

Install the dependencies

```sh
pip install -r requirements.txt
```

and good to go boi!

## Usage

Pick some picture, here we will use the black mage from the classic Final Fantasy game.

<img src="https://github.com/marekyggdrasil/colorswap/blob/main/examples/bmage.png?raw=true" width="135" heigth="208" style="image-rendering: pixelated;">

Start by extracting the palette by running

```sh
python extract.py examples/bmage.png examples/bmage_palette.png
```

it produces the following `bmage_palette.png` file in `examples` directory.

![original black mage palette](https://github.com/marekyggdrasil/colorswap/blob/main/examples/bmage_palette.png?raw=true)

Now we can change this palette, feel free to change those colors. For example the following one `examples/bmage_palette_disco.png`

![disco black mage palette](https://github.com/marekyggdrasil/colorswap/blob/main/examples/bmage_palette_disco.png?raw=true)

and we can run the color swap script that accepts original image, original palette, new palette and new image output file path

```sh
python swap.py examples/bmage.png examples/bmage_palette.png examples/bmage_palette_disco.png examples/bmage_disco.png
```

produces a `examples/bmage_disco.png` file

<img src="https://github.com/marekyggdrasil/colorswap/blob/main/examples/bmage_disco.png?raw=true" width="135" heigth="208" style="image-rendering: pixelated;">
