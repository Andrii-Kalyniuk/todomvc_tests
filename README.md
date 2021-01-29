[Todomvc.com](https://todomvc4tasj.herokuapp.com) web app
=========================================================
Todomvc is a simple web application for task management

Draft Test plan
---------------
### Features to be tested:
  * UI functionality map:
    - CRUD operations:
      - add                                  `!!!`
      - delete
        - one
          - by 'X' button                    `!!!`
          - by edit to blank                 `.`
        - all completed
          - by 'Clear-complete'              `!!!`
      - edit
        - text
          - submit
            - by Enter                       `!!`
            - by outside click               `.`
            - by Tab                         `.`
          - cancel edit by Esc               `!!!`
        - status
          - complete
            - one                            `!!`
            - all                            `.`
          - activate
            - one                            `.`
            - all                            `.`
    - storage todos
      - after page refresh                   `!!!`
    - filtering
      - active from                          `!`
        - completed
        - all
      - completed from                       `.`
        - active
        - all
      - all from                             `!`
        - active
        - completed
    - active item left counting
      - increment                            `!`
      - decrement                            `!`
      - unchanged                            `.`
  * ...
  > testing priority marks (ascending) - `. ! !! !!!`

### Feature not to be tested
  > Only basic todos management operations (CRUDs) are important
  > for the client's needs, so the detail on the functional map
  > and testing can now be omitted for:
  * todomvc app UI:
    - storage todos for the current session
    - filtering
      - different variations of transitions
      - and operations per filters
    - active item left counting
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

        2. edit 'a' to 'a edited'

        3. complete 'a edited'
        4. clear completed
           assert list: 'b', 'c'

        5. cancel edit 'c' to 'to be canceled'

        6. delete 'c'
           assert 'b'

    * ...
