response = str("y")
import random
while response == "y":
  response = input(str("Press 'y' to roll the dice and 'n' to exit"))
  no = random.randint(1,6)
  if no == 1:
    print("[--------]")
    print("[        ]")
    print("[    *   ]")
    print("[        ]")
    print("[--------]")
  elif no == 2:
     print("[--------]")
     print("[        ]")
     print("[   **   ]")
     print("[        ]")
     print("[--------]")
  elif no == 3:
     print("[--------]")
     print("[        ]")
     print("[   ***  ]")
     print("[        ]")
     print("[--------]")
  elif no == 4:
     print("[--------]")
     print("[        ]")
     print("[ *    * ]")
     print("[ *    * ]")
     print("[        ]")
     print("[--------]")
  elif no == 5:
     print("[-------]")
     print("[*     *]")
     print("[   *   ]")
     print("[*     *]")
     print("[-------]")
  elif no == 6:
     print("[--------]")
     print("[        ]")
     print("[*   *  *]")
     print("[*   *  *]")
     print("[        ]")
     print("[--------]")



















 
     
