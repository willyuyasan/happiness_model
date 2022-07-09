USE forms;

CREATE TABLE IF NOT EXISTS happiness_form (
    actual_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_form TEXT NOT NULL,
    name TEXT NOT NULL,
    words TEXT NOT NULL,
    age TEXT NOT NULL,
    genre TEXT NOT NULL,
    labor_status INTEGER NOT NULL
    
);

CREATE TABLE IF NOT EXISTS happiness_feedback (
    actual_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_form TEXT NOT NULL,
    real_happiness INTEGER NOT NULL,
    happiness_probability INTEGER NOT NULL
);
