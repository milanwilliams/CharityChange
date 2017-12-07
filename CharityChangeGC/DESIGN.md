Design can be broken up into Google Chrome Extension development and in web development. Let's first look at the former.

Google Chrome Extension - Design Choices

1. GCE Addition. My first major design choice was to have a GCE at all. I could have just created a website that operated similarly. But I didn't want the user to hunt around for another website. The beauty of a GCE is that it integrates seamlessly with existing websites. It is with this integration that I hoped for a higher likelihood of charitable donations. I decided that people would be more likely to donate if the option was more readily available.

2. A popup box. This box allows me to display additional information to the user. Currently, it is setup to host a charity of the month, but with increased versions, I would like to use it as ad space. These ads would increase the charitable donations and can also subsidize the overhead costs of integrating a payment processing API like Stripe. I designed this space both for its current implementation and to allow for future creativity.

3. Subtotal Insertion. I inserted a customized reminder above the subtotal, strategically placed so the user would have to notice it before completing a purchase. This reminder is customized to each purchase, providing the exact amount the user should donate. It links to the CharityChange website, again to ensure an easy transition from the familiar to the new.

Web Development - Design Choices

1. Register/Log In/Log Out. These pages allow users to create a personalized website experience. I added enhanced security to the passwords, by requiring a certain length and the inclusion of special characters. I also store their passwords in a hash, for safekeeping, to protect the safety of my users, especially as I am storing such highly sensitive material. The Log Out pages provides a similar safety experience, preventing anyone nearby from accessing the information unauthorized.

2. Index. Provides a handy welcome page to the user. Lists their prior transactions to remind them of prior charities they have donated to and previous amounts.

3. Donate. This page receives all of the different fields required by payment processing websites, like Stripe, and stores them in a database, to be later accessed. It checks to make sure all the fields have been properly filled to prevent any errors. It also saves each donation into a transaction database, a design decision to help the user see previous transaction amounts and where they've previously donated to.

4. Donated. Confirms to the user that the transaction has indeed gone through and the proper amount has been donated to the specified charity.

5. Transactions. Lists prior transactions, useful as a double-check to make sure the transaction submitted went through to the desired charity.

This is CharityChange.
