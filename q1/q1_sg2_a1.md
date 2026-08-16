9 - Pinatubo
#22 Dominguez, #23 Entac, #24 Fos
08/16/2026

Step 1
Main Problem:
The vending machine does not always work correctly, causing problems with payments, item selection, item availability, and machine speed.

Step 2
Sub-Problems:
1. The machine gives incorrect change after the payment.
2. The machine does not notify students when an item is sold out.
3. Students may press the wrong button and recieve the wrong item.
4. The machine becomes slow when multiple students use it at the same time.

Step 3
1. 
Sub-Problem: The machine gives incorrect change after payment.
CT Skill: Algorithms
Solution: We can use algorithms to use subtraction for payment. The equation would be money given - price of item = change. After this, we can make the machine dispense change using the biggest bill first.

2.
Sub-Problem: The machine does not notify the students when an item is sold out.
CT Skill: Abstraction
Solution: We can set up a counter for each item and when one is sold out, it can display an “OUT OF STOCK” sign either on the LCD or beside the price of the item in the vending machine (if there’s no LCD.)

3.
Sub-Problem: We can set up a counter for each item and when one is sold out, it can display an “OUT OF STOCK” sign either on the LCD or beside the price of the item in the vending machine (if there’s no LCD.).
CT Skill: Pattern Recognition
Solution: We can set up a counter for each item and when one is sold out, it can display an “OUT OF STOCK” sign either on the LCD or beside the price of the item in the vending machine (if there’s no LCD.)

4.
Sub-Problem: The machine slows down when it is used continuously by student after student.
CT Skill: Algorithms
Solution: We can add a quick cooldown timer so that the vending machine can fully clear its memory before the next order.

Step 4
assume item = price of what the student wants
              money = how much the student gives 
              change = money-item (amount of change to be given by the machine)

if item is picked:

              if change==0:
                            drop item
                            does not print and drop change
              elif: change>0:
                            drops item
                            prints and drops change
              else: 
                            break
