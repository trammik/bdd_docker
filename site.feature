Feature: Demo site login and basic functionality

  Scenario: Login
  Given We navigated to the site
  When We fill the login and pass fields with correct data
  And We press login button
  Then We are successfully logged in

  Scenario: Add to cart
  Given We are logged in
  When We add product to the cart
  And We press on cart icon
  Then Product appears in cart


  Scenario: Bad login
  Given We navigated to the site
  When We fill the login and pass fields with invalid data
  And We press login button
  Then We got an error message and not logged in

