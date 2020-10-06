const { query } = require('express');
var express = require('express');
var router = express.Router();

 //Check against the data from the database.
 //If it matches this will return a JSON bodywith status code 200. Otherwise it will return a 403(forbidden)

const users[] = query('SELECT * FROM auth_log WHERE');
/* POST */
router.post('/', (req, res) => {

connection.connect();

users=[];

app.get('/', function(req, res){
    connection.query(
    'SELECT * FROM auth_log WHERE nemId = [req.body.nemId]',
    function(err, result)
    {
        if(err) throw err;
        res.render('test',{nemId:"", users:result});
        aUser = result;
    });
});


    const random_code =  Math.floor(Math.random() * 899999 + 100000)
    const user = users.find(user.nemId, user.nemIdCode = req.body.nemId, req.body.nemIdCode) 
    if(user == null){
        return res.statusCode(403)
    } else{
        res.statusCode(200)
        res.json(random_code)
    }
} 
);
module.exports = router;