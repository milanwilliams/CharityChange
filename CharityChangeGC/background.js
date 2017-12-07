// Listening for when the page changes
chrome.runtime.onInstalled.addListener(function() {
  chrome.declarativeContent.onPageChanged.removeRules(undefined, function() {
    chrome.declarativeContent.onPageChanged.addRules([{
      conditions: [
        // When on Amazon's Cart page...
        new chrome.declarativeContent.PageStateMatcher({
          pageUrl: { hostEquals: 'www.amazon.com',  urlContains: 'gp/cart/view.html/ref=nav_cart', schemes: ['https'] },

        })
      ],
      // ... show the page action.
      actions: [new chrome.declarativeContent.ShowPageAction() ]
    }]);
  });
});
// Allows for testing within the web console
console.log('loaded')
