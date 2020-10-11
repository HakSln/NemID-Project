var express = require('express');
var router = express.Router();

 //Check against the data from the database.
 //If it matches this will return a JSON bodywith status code 200. Otherwise it will return a 403(forbidden)

//const users[] = query('SELECT * FROM auth_log WHERE');
/* POST */
router.post('/', (req, res) => {

    const random_code =  Math.floor(Math.random() * 899999 + 100000)

    var myNemId = req.body.NemId;

req.connection(function(err, connection)
{
    if (err) throw err;     
    connection.query("SELECT NemID FROM user WHERE NemId =" + myNemId, 
    function(results) {    
    if (results) {
        res.statusCode(200)
        res.json(random_code)
    } 
    else{
        return res.statusCode(403)}
    });
})

// users=[]= query('SELECT * FROM auth_log WHERE ');
//var user = users.find(user.nemId, user.nemIdCode = req.body.nemId, req.body.nemIdCode
//app.get('/', function(req, res){
//    connection.query(
//    'SELECT * FROM auth_log WHERE nemId = [req.body.nemId]',
//    function(err, result)
//    {
//        if(err) throw err;
//        res.render('test',{nemId:"", users:result});
//        aUser = result;
//    });
//});


    
    //const user = users.find(user.nemId, user.nemIdCode = req.body.nemId, req.body.nemIdCode) 
    //if(user == null){
    //    return res.statusCode(403)
    //} else{
    //    res.statusCode(200)
    //    res.json(random_code)
   // }
} 
);
module.exports = router;