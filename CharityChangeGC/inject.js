//
chrome.extension.sendMessage({}, function(response) {
	var readyStateCheckInterval = setInterval(function() {
	if (document.readyState === "complete") {
		clearInterval(readyStateCheckInterval);

    //Useful for testing the extension
    console.log('Extension loaded');

        // Gets the price element out of the Amazon webpage
        var target = document.getElementsByClassName('a-size-medium a-color-price sc-price sc-white-space-nowrap  sc-price-sign');

        //Ensures the target exists as an element
        if (target.length !== 0){
            subTotal = target[0]; //DOM element
            price = subTotal.innerText; //Text element

            //Useful for testing the extension
            console.log("Here is the price!", price)

            //Finds the change from the price
            price = price.replace('$','')
            price = price.split('.')[1]
            price = Number(price)
            price = 100-price

            var parent  = subTotal.parentElement;
            var div = document.createElement('div');

            //Sends user to the CharityChange website, includes change in URL as a reminder to user of amount
            div.innerHTML = '<a href="http://ide50-milanwilliams.cs50.io:8080/donate?price='+price+'"><span class="xa-declarative" style="font-size: 13px;display: block;">Make a CHANGE! Donate '+price+' cents to charity!</span></a>';
            parent.appendChild(div);

        }
	}
	}, 10);
});
