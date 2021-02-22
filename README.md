[Todomvc.com](https://todomvc4tasj.herokuapp.com) web app
=========================================================
Todomvc is a simple web application for task management

Draft Test plan
---------------
### Features to be tested:
  * UI functionality map:
    - CRUD operations:
      - add                                  `!!!` `e2e` `f`
      - delete
        - one
          - by 'X' button                    `!!!` `e2e` `f`
          - by edit to blank                 `.`         `f`
        - all completed
          - by 'Clear-complete'              `!!!` `e2e` `f`
      - edit
        - text
          - submit
            - by Enter                       `!!`  `e2e` `f`
            - by loose focus                 `.`         `f`
              - by outside click
              - by Tab
          - cancel edit by Esc               `!!!` `e2e` `f`
        - status
          - complete
            - one                            `!!`  `e2e` `f`
            - all                            `.`         `f`
          - activate
            - one                            `.`         `f`
            - all                            `.`         `f`
    - storage todos
      - after page refresh                   `!!!`       `f`
    - filtering
      - active from                          `!`         `f`
        - completed
        - all
      - completed from                       `.`         `f`
        - active
        - all
      - all from                             `!`         `f`
        - active
        - completed
    - active items left counting
      - increment                            `!`         `f`
      - decrement                            `!`         `f`
      - unchanged                            `.`
  * ...
  > testing priority marks (ascending) - `. ! !! !!!`  
  > coverage by
  >  - `e2e` - end-to-end test 
  >  - `f` - feature test

### Feature not to be tested
  > Only basic todos management operations (CRUDs) are important
  > for the client's needs, so the detail on the functional map
  > and testing can now be omitted for:
  * todomvc app UI:
    - filtering
      - different variations of transitions
      - and operations per filters
  * ...

### Environmental needs
  * Python => '3.7'
  * Pytest => '5.2'
  * Selene => '1.0.2'

### Testing tasks
    * Scenario: "User's usual workflow, basic todos management (CRUD)"
      The user add, edit, complete and delete a few todos.

      GIVEN open Todomvc

        1. add 'a', 'b', 'c'
           assert list: 'a', 'b', 'c'

        2. edit 'b' to 'b edited'

        3. complete 'b edited'
        4. clear completed
           assert list: 'a', 'c'

        5. cancel edit 'c' to 'to be canceled'

        6. delete 'c'
           assert 'a'

    * ...
