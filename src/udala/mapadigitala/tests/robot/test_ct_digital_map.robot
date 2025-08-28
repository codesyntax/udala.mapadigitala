# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s udala.mapadigitala -t test_digital_map.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src udala.mapadigitala.testing.UDALA_MAPADIGITALA_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/udala/mapadigitala/tests/robot/test_digital_map.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a DigitalMap
  Given a logged-in site administrator
    and an add DigitalMap form
   When I type 'My DigitalMap' into the title field
    and I submit the form
   Then a DigitalMap with the title 'My DigitalMap' has been created

Scenario: As a site administrator I can view a DigitalMap
  Given a logged-in site administrator
    and a DigitalMap 'My DigitalMap'
   When I go to the DigitalMap view
   Then I can see the DigitalMap title 'My DigitalMap'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add DigitalMap form
  Go To  ${PLONE_URL}/++add++DigitalMap

a DigitalMap 'My DigitalMap'
  Create content  type=DigitalMap  id=my-digital_map  title=My DigitalMap

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the DigitalMap view
  Go To  ${PLONE_URL}/my-digital_map
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a DigitalMap with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the DigitalMap title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
