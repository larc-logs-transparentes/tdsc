dbbuservice = connect( 'mongodb://localhost/bu_service' );

dbbuservice.createUser(
  {
    user: "buuser",
    pwd: "bupassword", 
    roles: [ { role: "readWrite", db: "bu_service" }]
  }
);

dbtlmanager = connect( 'mongodb://localhost/tlmanager' );

dbtlmanager.createUser(
  {
    user: "tluser",
    pwd: "tlpassword", 
    roles: [ { role: "readWrite", db: "tlmanager" }]
  }
);
