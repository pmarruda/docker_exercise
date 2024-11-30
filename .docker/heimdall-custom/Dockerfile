FROM linuxserver/heimdall

# Copy the entire pre-configured /config directory
COPY heimdall-config /defaults/config

# Copy the startup script to handle first-run initialization
COPY init/copy-config /etc/cont-init.d/copy-config

# Ensure the script has execution permissions
RUN chmod +x /etc/cont-init.d/copy-config
