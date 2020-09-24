var count =0
var input = document.getElementById("input")
var ul = document.getElementById("list")


function listFunction(){
var reWhiteSpace = new RegExp("/^\s+$/");
if(input.value.length <=0 || input.value.indexOf(' ') >= 0){
	alert("Please provide the valid input");
  return 
}
count +=1
var listViewItem=document.createElement('li');
listViewItem.append(input.value)
list.appendChild(listViewItem)
input.value = ""
 
 if(count%3 == 0){
listViewItem.style = "color:red;"
 }
  
}