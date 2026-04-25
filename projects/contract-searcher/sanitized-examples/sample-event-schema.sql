CREATE TABLE bid_events (
    event_id TEXT PRIMARY KEY,
    title TEXT,
    agency TEXT,
    due_date TEXT,
    status TEXT,
    relevance_score INTEGER,
    processing_status TEXT,
    last_error TEXT
);
