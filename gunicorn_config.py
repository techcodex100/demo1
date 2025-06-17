import multiprocessing

# Server socket
bind = "0.0.0.0:10000"
backlog = 2048

# Worker processes
workers = 1  # Using single worker for better stability
worker_class = "uvicorn.workers.UvicornWorker"
worker_connections = 1000
timeout = 120  # Increased timeout for PDF generation
keepalive = 2

# Logging
accesslog = "-"
errorlog = "-"
loglevel = "debug"  # Changed to debug for better error tracking

# Process naming
proc_name = "pdf_generator"

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Application
wsgi_app = "app:application" 