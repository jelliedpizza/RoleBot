until python3.5 brain.py; do
    echo "crashed with exit code $?.  Respawning.." >&2
    sleep 1
done