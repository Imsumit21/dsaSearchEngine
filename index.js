//Requiring the modules -> It should always be done on the top
const express = require("express");
const ejs = require("ejs"); //View Engine
const path = require("path");

//Creating our server
const app = express();

app.use(express.json());

//Setting Up EJS
// Require static assets from public folder
app.use(express.static(path.join(__dirname, 'public')));

// Set 'views' directory for any views 
// being rendered res.render()
app.set('views', path.join(__dirname, 'views'));

app.set("view engine", "ejs");

// app.use(express.static(path.join(__dirname, "/public")));

const PORT = process.env.PORT || 3003;

// GET, POST, PATCH, DELETE

//@GET /
//description: GET request to home page
app.get("/", (req, res) => {
  res.render("index");
});

app.get("/search", (req, res) => {
  const query = req.query;

  const question = query.question;
  // console.log(question);
  //TF-IDF ALgo



  //List of 5 questions

  setTimeout(() => {
    const fs = require('fs');
    TfIdf = require('tf-idf-search');
    var array1= fs.readFileSync('IB_problem_urls.txt').toString().split("\n");
    var array2= fs.readFileSync('IB_problem_titles.txt').toString().split("\n");
    tf_idf = new TfIdf();
    const arr = [];
    for(let i = 1; i <= 90; i++) 
    {
        if (i==269)
        {
            continue;
        }
        const t="./IB_problem" + i.toString() + ".txt";
        arr.push(t);
    }
    for(let i = 126; i <= 140; i++) 
    {
        
        const t="./LC_problem" + i.toString() + ".txt";
        arr.push(t);
    }
    const disp=[];
    var corpus = tf_idf.createCorpusFromPathArray(arr);
    const content= question;
    var search_result = tf_idf.rankDocumentsByQuery(content);
    //console.log(search_result);
    for(let i = 0; i < 5; i++) 
    {
        //console.log(search_result[i].index);
        // console.log(array[search_result[i].index]);
        const str1=(i+1).toString();
        const str2=array2[search_result[i].index];
        const str3= str1+' '+')'+' '+str2;
        disp.push({url:array1[search_result[i].index],title:str3});
    }
    
    // console.log(disp);
    res.json(disp);
  }, 3000);
});

//Assigning Port to our application
app.listen(PORT, () => {
  console.log("Server is running on port " + PORT);
});
