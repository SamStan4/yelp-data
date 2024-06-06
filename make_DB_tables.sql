CREATE TABLE _business (
    business_id VARCHAR(25),
    business_name VARCHAR(50),
    business_address VARCHAR(100),
    business_state VARCHAR(15),
    business_city VARCHAR(50),
    business_postal_code INT,
    business_longitude FLOAT,
    business_latitude FLOAT,
    business_stars FLOAT,
    business_review_count INT,
    business_is_open BOOLEAN,
    PRIMARY KEY (business_id)
);

CREATE TABLE _category (
    business_id VARCHAR(25),
    category_name VARCHAR(100),
    category_truth_value BOOLEAN,
    PRIMARY KEY (business_id, category_name),
    FOREIGN KEY (business_id) REFERENCES _business(business_id)
);

CREATE TABLE _hours (
    business_id VARCHAR(25),
    hours_day VARCHAR(10),
    hours_open CHAR(5),
    hours_close CHAR(5),
    PRIMARY KEY (business_id, hours_day),
    FOREIGN KEY (business_id) REFERENCES _business(business_id)
);

CREATE TABLE _attribute (
    business_id VARCHAR(25),
    attribute_name VARCHAR(50),
    attribute_truth_value BOOLEAN,
    PRIMARY KEY (business_id, attribute_name),
    FOREIGN KEY (business_id) REFERENCES _business(business_id)
);

CREATE TABLE _user (
    user_id VARCHAR(25);
    user_name VARCHAR(25);
    user_yelping_since DATE;
    user_review_count INT,
    user_fanse INT,
    user_average_stars FLOAT,
    user_funny INT,
    user_useful INT,
    user_cool INT,
    PRIMARY KEY (user_id)
);

CREATE TABLE _review (
    business_id VARCHAR(25),
    user_id VARCHAR(25),
    review_id VARCHAR(25),
    review_stars FLOAT,
    review_date DATE,
    review_text VARCHAR(3000),
    review_useful INT,
    review_funny INT,
    review_cool INT,
    PRIMARY KEY (review_id),
    FOREIGN KEY (user_id) REFERENCES _user(user_id),
    FOREIGN KEY (business_id) REFERENCES _business(business_id)
);

CREATE TABLE _check_in (
    business_id VARCHAR(25),
    check_in_day VARCHAR(10),
    check_in_start TIME,
    check_in_stop TIME,
    check_in_total INT,
    PRIMARY KEY (business_id, check_in_day),
    FOREIGN KEY (business_id) REFERENCES _business(business_id)
);