FROM evalai_django

CMD ["./docker/wait-for-it.sh", "django:8000", "--", "sh", "/code/docker/vm/celery/container-start.sh"]
