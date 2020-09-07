const express = require('express')
const mongodb = require('mongodb')

const MongoClient = mongodb.MongoClient
const connectionURL = process.env.connectionURL
const databaseName = process.env.databaseName

const app = express()
const port = process.env.PORT || 3000

app.use(express.json())

app.listen(port, () => {
    console.log('Server is Running! on ' + port)
})

app.get('/v1/data', (req, res) => {

    const skip = req.body.skip
    const limit = req.body.limit
    const order = req.body.order

    MongoClient.connect(connectionURL, { useNewUrlParser: true }, (error, client) => {
        if (error) {
            console.log('Unable to connect to database!')
            res.json({
                'data': {}
            });
        }
        const db = client.db(databaseName)
       
        db.collection('occ').find({}).sort({ 'meta.download_latency': order }).skip(skip).limit(limit).toArray((error, data) => {
            res.json({
                'data': data
            });
          })
       })
})

app.get('/v1/data/search', (req, res) => {

    const keyword = req.body.keyword
    const searchTerm = `keywords.${keyword}`

    const skip = req.body.skip
    const limit = req.body.limit
    const order = req.body.order

    MongoClient.connect(connectionURL, { useNewUrlParser: true, useUnifiedTopology: true }, (error, client) => {
        if (error) {
            console.log('Unable to connect to database!')
            res.json({
                'data': {}
            });
        }
        const db = client.db(databaseName)  
        console.log(searchTerm);
       
        db.collection('occ').find({[searchTerm]: { $gt: 0 }}).sort({ 'meta.download_latency': order }).skip(skip).limit(limit).toArray((error, data) => {
            res.json({
                'data': data
            });
          })
       })
})

