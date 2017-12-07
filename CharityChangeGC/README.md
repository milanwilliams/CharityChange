Hello, welcome to CharityChange.

CharityChange is a Google Chrome Extension that rounds up your current purchases to the nearest dollar and donates that money to a charity of your choosing.

To download the extension, please install the package titled "CharityChangeGC". This contains all the information surrounding the Google Chrome Extension implementation. Let's begin an in-depth look at each of the files in this folder.

background.js - This file specifies the pages that CharityChange is valid on. For our first version, CharityChange works within the Amazon Shopping Cart. Add an item into the cart, and CharityChange will add a handy a suggestion for how much money you should donate.

icon16/48/128.png - These files specify the CharityChange icon with different sizes used for different areas within Chrome.

inject.js - This file 'injects' the Amazon page with a link to the official CharityChange website. It prompts the user by getting the 'change' that the user could be donating to charity.

manifest.json - This file establishes the Google Chrome Extensions according to the Chrome Extension API. It specifies the title, version number, description, icon, and sets basic permissions and scripts to be run.

popup.html - Provide a popup addition to the Chrome Extension, offers a featured Charity of the Month to help the user decide where to donate!

Once you have downloaded these files and feel comfortable with their intended implementation, visit chrome://extensions in your Chrome browser. Ensure that you are in Developer Mode by clicking the checkbox in the top right-hand corner. Click Load unpacked extension. Navigate to the directory where CharityChange is located and select it to open. To make sure you are working in the most up-to date version of Charity Change, click Reload (⌘R).

Next, let's take a look at the website, Charity Change itself! Download the package titled "CharityChangeWeb" in the CS50 IDE. This contains all the information surrounding the CharityChange website. Let's begin an overview of this folder. Details are explained in DESIGN.md.

With the folder downloaded into the CS50 IDE, use the terminal and cd to get into the directory you have saved it under. At the command line, input 'flask run' to launch the website. Flask will provide a link to where it is hosting the website. Click this link to view.


If you are a new user, take the time to register, by clicking on the "Register" icon in the upper left-hand corner. Don't forget your password, once it has been set, we cannot send it to you for your own security and the security of our other users. You will have to make a new account :(. You should be logged in automatically. Once logged in, you will be greeted by our inspirational homepage. It will display (if any) of your past transactions, detailing the amount you donated and what charity you donated to. You can view the these same past transactions by clicking on "Past Donations" in the navigation bar at the top of the screen.

To make another donation, click the "Donate" page. Once there, please input the information requested (name, address, charity, amount card number and type, CVC, and expiration date). Once inputted this information will be saved to a database, which in future versions, will connect to a payment processing service, to properly facilitate the transfer of funds. After you have donated, you will be shown a confirmation page to ensure your transaction has properly completed. Once you are done, don't forget to log out at the top of the screen!

NOTE: In order for the Chrome Extension to work seamlessly with the CS50, open up inject.js. Take care to change the username [ide50-username.cs50.io] to reflect YOUR workspace. Flask must also be running throughout your usage of the Chrome Extension. It will not work otherwise. Once you have done this, go to the Amazon Shopping cart, and click the link above 'SubTotal' to go to the Charity Change website.

This is CharityChange.
