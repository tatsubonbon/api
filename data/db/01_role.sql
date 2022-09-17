INSERT INTO
    `Role` (
        `id`,
        `name`,
        `default`,
        `permissions`,
        `created_at`
    )
VALUES (
        1,
        'User',
        1,
        7,
        CURRENT_TIMESTAMP
    );

INSERT INTO
    `Role` (
        `id`,
        `name`,
        `default`,
        `permissions`,
        `created_at`
    )
VALUES (
        2,
        'Moderator',
        0,
        15,
        CURRENT_TIMESTAMP
    );

INSERT INTO
    `Role` (
        `id`,
        `name`,
        `default`,
        `permissions`,
        `created_at`
    )
VALUES (
        3,
        'Administrator',
        0,
        31,
        CURRENT_TIMESTAMP
    );