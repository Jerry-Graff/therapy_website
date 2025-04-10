FROM certbot/certbot

# Copy the auto-renew entrypoint script into the image
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use the entrypoint for auto-renewal
ENTRYPOINT ["/entrypoint.sh"]