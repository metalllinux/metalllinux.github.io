---
title: "udev rule instructions"
category: "general-linux"
tags: ["udev", "rules", "thrustmaster", "16000m"]
---

### udev rule instructions

* Open a terminal.

* Run the command `lsusb | grep -i thrustmaster`

* You'll then see on the right of the word `ID` and on the left of the word `Thrustmaster` a string of numbers and letters like this (yours will be different):
```
044f:b10a
```

* You should see two results, one for the joystick and one for the throttle.

* Of note, the Product ID part in the above example is b10a

* The Vendor ID part is the 044f portion.

* Make a note of the above IDs. These will be needed for the steps below.

* Add your PC user to the `input` group:
```
sudo usermod -a -G input <YOUR_ACCOUNT_USERNAME>
```

* Run the following command to create the `udev` rules. BEFORE running the command, fill in where it says <YOUR_VENDOR_ID_HERE> and <YOUR_PRODUCT_ID_HERE> with the values you found from the `lsusb` command from above.
```
cat << "EOF" | sudo tee /etc/udev/rules.d/99-thrustmaster-t16000m.rules
SUBSYSTEM=="usb", ATTRS{idVendor}=="<YOUR_VENDOR_ID_HERE>", MODE="0666"

# Thrustmaster T16000M Joystick
KERNEL=="event*", ATTRS{idProduct}=="<YOUR_PRODUCT_ID_HERE>", ATTRS{idVendor}=="YOUR_VENDOR_ID_HERE", MODE="0666" GROUP="input"

# Thrustmaster T16000M Joystick
KERNEL=="event*", ATTRS{idProduct}=="<YOUR_PRODUCT_ID_HERE>", ATTRS{idVendor}=="YOUR_VENDOR_ID_HERE", MODE="0666" GROUP="input"
EOF
```

* An example is below:

```
cat << "EOF" | sudo tee y
SUBSYSTEM=="usb", ATTRS{idVendor}=="044f", MODE="0666"

# Thrustmaster T16000M Joystick
KERNEL=="event*", ATTRS{idProduct}=="b10a", ATTRS{idVendor}=="044f", MODE="0666" GROUP="input"

# Thrustmaster T16000M Throttle
KERNEL=="event*", ATTRS{idProduct}=="c12g", ATTRS{idVendor}=="044f", MODE="0666" GROUP="input"
EOF
```

* When copying and pasting the above command, highlight and copy everything from where it says `cat` to `EOF` and then paste the whole output into the terminal and press enter.

* Then run this command:
```
sudo udevadm control --reload
```

* Log out and then log back in again.

* Boot up Steam and check that the joystick is recognised and see if it is also seen in

* Please show me the output of `lsusb | grep -i thrustmaster` and also `sudo cat /etc/udev/rules.d/99-thrustmaster-t16000m.rules` afterwards.
