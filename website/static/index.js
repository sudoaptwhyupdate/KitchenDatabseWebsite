function deleteItem(itemId) {
  //sends a basic request to the back end
  fetch('/delete-item', {
    method: 'POST',
    body: JSON.stringify({ itemId: itemId })
  }).then((_res) => {
    //redirect to the home page, refreshes the page
    window.location.href = "what_you_have";
  });
}