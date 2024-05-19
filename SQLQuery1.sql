CREATE DATABASE PhelieuDatabase;
USE PhelieuDatabase;

CREATE TABLE sat_vun (
    id INT PRIMARY KEY IDENTITY(1,1),
    ten_sat NVARCHAR(255),
    don_gia text
);

drop table sat_vun

USE PhelieuDatabase;
GO

CREATE PROCEDURE InsertSatVun
    @ten_sat NVARCHAR(255),
    @don_gia FLOAT
AS
BEGIN
    INSERT INTO sat_vun (ten_sat, don_gia)
    VALUES (@ten_sat, @don_gia);
END;

create procedure selectdata
AS
BEGIN
    select * from sat_vun;
END;
