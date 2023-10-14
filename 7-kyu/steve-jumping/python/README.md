   # Description
   Steve, from minecraft, is jumping down from blocks to blocks and can get damages at each jump. Damage depends on `distance` between blocks and `block type` he jumped on. The goal is to know if he survives his descent or not.

You are given a list of `N` blocks as strings, in the format `'BLOCK_HEIGHT BLOCK_TYPE'`. Steve jumps from one block to the next, and get damages calculated with the following formula:
  
    DMG = max(0, (DISTANCE - 3.5) * (1 - DMG_REDUCTION))
  
  The distance is calculated as the difference between the `height` of the current and the next block. DMG should be **rounded down** to the nearest integral. 
  
  `DMG_REDUCTION` depends on `BLOCK_TYPE`:
  
    BLOCK_TYPE --> DMG_REDUCTION
    'D' --> 0 #Dirt block
    'B' --> 0.5 #Bed
    'H' --> 0.8 #Hay block
    'W' --> 1 #Water block
  
  ## Task
  
  Write a function, that returns the outcome for Steve:

  - If he survives, it returns `'jumped to the end with X remaining HP'`, where `X` is the remaining HP at the end of the array.
  - If he dies before the end of the array, it returns `'died on I'`, where `I` is the index of the jump he dies.
  
  ### Rules
  
  - Steve has `20 HP` at the start. If `HP` drops below or equal `0`, Steve dies. 
  - `BLOCK_TYPE` can be `'D'` or `'B'` or `'H'` or `'W'` only.
  - `N` cannot be less than `2`.
  - `BLOCK_HEIGHT[i]` cannot be less than `BLOCK_HEIGHT[i+1]` and always non-negative integral.
  - All inputs are valid according to the rules.
  
  #### Examples (input --> output)
    
    ['10 D', '4 D', '0 D'] --> 'jumped to the end with 18 remaining HP'     
        |      |      |
        |      |   The third block with height 0 and type D
        |   The second block with height 4 and type D
     The first block with height 10 and type D
     
     /*All blocks are type D, so DMG_REDUCTION will be 0 for all cases
     DISTANCE on the first jump will be 10 - 4 = 6
     DMG on the first jump will be max(0, (6 - 3.5) * (1 - 0)) = 2.5 -> 2 (rounding down)
     DISTANCE on the second jump will be 4 - 0 = 4
     DMG on the second jump will be max(0, (4 - 3,5) * (1 - 0)) = 0.5 -> 0 (rounding down)
     So HP in the end will be 20 - 2 - 0 = 18*/
     
     
    ['100 D', '50 H'] --> 'jumped to the end with 11 remaining HP'
    
    ['999 D', '0 W'] --> 'jumped to the end with 20 remaining HP'
    
    ['999 D', '0 D'] --> 'died on 1'