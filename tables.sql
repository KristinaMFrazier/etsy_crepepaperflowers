-- LISTINGS_MAIN

CREATE TABLE public.listings_main_11282020
(
    main_id integer,
    listing_id "char",
    user_id "char",
    title "char",
    description "char",
    price,
    currency_code "char",
    quantity,
    url "char",
    views,
    num_favorers,
    who_made "char",
    when_made "char",
    item_weight_unit,
    recipient,
    occasion,
    taxonomy_path,
    is_vintage
    PRIMARY KEY (main_id)
);

ALTER TABLE public.listings_main_11282020
    OWNER to postgres;
