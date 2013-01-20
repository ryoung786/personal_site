<?php 
  $feedURL = "http://rss.cnn.com/rss/cnn_topstories.rss";  
if($_GET['feed'] == "1")
{ 
	$feedURL = "http://rss.cnn.com/rss/cnn_topstories.rss"; 
}

$getFeed = curl_init($feedURL); 
$result = curl_exec($getFeed); 
curl_close($getFeed); 
echo $result; 
  
?> 