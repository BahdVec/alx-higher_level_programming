
# Technical Screener, Enterprise / Premium Support

The following is a series of customer questions, most of them coming from real customer interactions. For each question, write a customer-facing response. For questions that you don't know the answers to, feel free to search for answers online and provide the sources you used. Do not invent facts and do not be afraid to ask the customer for information, if needed.

We will be looking at overall content, ability to research technical questions, ability to present a professional yet friendly response to customers, and your ability to intuit details based on very limited information. This questionnaire should take no more than two hours to complete. If you get stuck, don't be afraid to ask us to clarify anything.

A few things to keep in mind:

- It should always be clear to the person on the other side of the computer that you are a smart, friendly, and awesome person.
- Responses should not contain unneeded filler, yet should not be overly brief. They should be complete.
- Responses should have a greeting and closing.
- GitHub is spelled with a capital G and a capital H.
- GitHub is classy. When in doubt: be classy.

## Question 1

You receive the following ticket from a customer:

> Hi GitHub! So according to the docs at [https://docs.github.com/enterprise-server/rest/reference/teams#add-or-update-team-repository-permissions](https://docs.github.com/enterprise-server/rest/reference/teams#add-or-update-team-repository-permissions), I should be able to add teams to a repo programmatically.
>
> However, this does not work when using the following code:
>
> curl -H "Authorization: token BLAHBLAHBLAH" -H "Content-Length: 0" -X put -d "" [https://hostname/api/v3/organizations/10/team/23/repos/jimmy/some-repo-name](https://hostname/api/v3/organizations/10/team/23/repos/jimmy/some-repo-name)
>
> Could someone give me a curl one liner that lets me add teams to repos ? Or at least tell me what facet of the documentation has escaped me for the last 45 minutes?

## Question #1 response

Hi There,

Thank you for contacting GitHub Enterprise Technical Support. 
My name is Philip Badu, and I am the Support Engineer assigned to your service request.

I understand that you are experiencing issues while trying to add teams to a repo programmatically.

Checking the code you shared, please find below possible reason that
 could stop the code from working as expected;

After the review of the code you shared, here are my findings:

1\. You are using the put method instead of the PUT method. The HTTP
methods are case-sensitive and should be written in uppercase. Using
lowercase may result in a bad request or a method not allowed error.

2\. You are using the wrong URL for the API endpoint. The correct URL
for updating team repository permissions is
<https://hostname/api/v3/orgs/:org/teams/:team_slug/repos/:owner/:repo>.
Please replace the placeholders with the actual values.

3\. Your code includes the Content-Length header, which is not listed as
required in the documentation. The Content-Length header specifies the
size of the request body in bytes, but you are not sending any data in
the body. This could cause the code to fail.

4\. In your URL for the API endpoint, you are using organizations
instead of orgs, team instead of teams.

A correct command should look like this:

curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer <BLAHBLAHBLAH>" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  [https://hostname/api/v3/orgs/10/teams/23/repos/jimmy/some-repo-name](https://hostname/api/v3/orgs/10/teams/23/repos/jimmy/some-repo-name)

You can access the latest API documentation by visiting this page
[add-or-update-team-repository-permissions](https://docs.github.com/en/enterprise-server@3.10/rest/teams/teams?apiVersion=2022-11-28#add-or-update-team-repository-permissions).
A detailed sample code is provided for your guidance.

If you encounter any difficulties again while applying the code, please
do not hesitate to reach out to me.

Thank you for choosing GitHub Enterprise.

Best regards,

Philip Badu

GitHub Enterprise Support Team

## Question 2

You receive the following ticket from a customer with 1000 GitHub Enterprise Server seats:

> Hi GitHub,
>
> We are experiencing serious performance issues and receiving multiple complaints from our developers.
>
> Browsing the web interface often results in timeouts and Git operations are taking magnitudes longer than usual to complete.
>
> $ free -m total used free shared buffers cached Mem: 15331 14648 683 0 149 6170 -/+ buffers/cache: 8328 7003 Swap: 0 0 0 $ uptime 10:50:08 up 123 days, 25 min, 1 user, load average: 6.25, 5.51, 3.75

What could be causing these performance issues? What would you recommend doing to mitigate these issues?

Notes

You do not have shell or web interface access to their GitHub Enterprise instance.

## Question #2 response

Hi There,

Thank you for contacting GitHub Enterprise Technical Support. 
My name is Philip Badu, and I am the Support Engineer assigned to your service request.

I understand that you are experiencing issues relating to performance as the web interface times out and Git operations taking longer than usual to get completed.

**Possible Causes of Performance Issues:**

1\. **Server Resources**: The server\'s resource utilization, as
indicated by the \`free\` and \`uptime\` commands, suggests high memory
usage and a moderately high load average. This could be due to
insufficient resources for your large user base.

2\. **Network Latency**: Slow web performance may be due to network issues like high latency or bandwidth constraints. You can diagnose this using these commands:
For latency measurement:

```bash
ping github.com
```

For network tracing:

```bash
traceroute github.com
```

For a detailed network diagnostic:

```bash
mtr github.com
```

Replace `github.com` with the relevant domain or IP address.

3\. **Repository Size**: Large repositories with numerous files and history can slow down Git operations. It is essential to manage and optimize repositories, particularly if you have a significant amount of data.
To optimize and manage repositories effectively, consider using these Git commands:

1. To remove untracked files:

```bash
git clean -f -n   # Preview untracked files to be removed
git clean -f      # Remove untracked files
```

2. To compress the repository and remove unnecessary objects:

```bash
git gc --aggressive --prune=now
```

3. To limit the depth of commit history:

```bash
git clone --depth <depth> <repository_URL>
```

4. To filter and rewrite repository history:

```bash
git filter-repo --path <path_to_keep> --path-rename <old_path>:<new_path>
```

By using these commands, you can efficiently optimize and manage your repositories, ensuring smoother Git operations.

**Recommendations to Mitigate Performance Issues:**

1\. **Server Resources**:

1. Evaluate your server's current resource allocation and consider upgrading CPU, RAM, or storage to meet the demands of your user base.
    - To check the current CPU information:

    ```bash
    cat /proc/cpuinfo
    ```

    - To view the available memory (RAM):

    ```bash
    free -h
    ```

    - For disk space information:

    ```bash
    df -h
    ```

2. Monitor system resource usage to identify which resources are bottlenecking your server's performance.
    - To monitor CPU usage:

    ```bash
    top
    ```

    - For a more detailed CPU usage breakdown:

    ```bash
    mpstat -P ALL 1
    ```

    - To monitor RAM usage:

    ```bash
    htop
    ```

    - To check disk I/O usage:

    ```bash
    iostat -dx 1
    ```

    - To monitor network activity:

    ```bash
    iftop
    ```

These commands will help you assess your server's resource allocation and identify any performance bottlenecks. Depending on your findings, you can then plan upgrades or optimizations accordingly.

2\. **Network Optimization**:

- Review your network infrastructure to ensure it can handle the traffic from the number of users in your organization. Consider increasing bandwidth if needed.
  - To check bandwidth usage:

    ```bash
    netstat -i
    ```

- Optimize network routes and reduce latency where possible to enhance the web interface's responsiveness.
  - To optimize network routes:

    ```bash
    traceroute <destination>
    ```

  - To reduce latency, consider using content delivery networks (CDNs) or optimizing your network configuration.

3\. **Repository Optimization**:

- Check the size and complexity of your repositories. If they are large, consider using Git LFS for binary assets and exploring ways to split large repositories into smaller, more manageable ones:

  ```bash
  git count-objects -v
  ```

- Implement Git LFS for binary assets:

  ```bash
  git lfs install
  git lfs track "*.bin"   # Track binary files
  git add .gitattributes  # Stage .gitattributes file
  git commit -m "Enable Git LFS"
  ```

- Split large repositories into smaller ones:

  ```bash
  git clone --mirror <source_repo_URL>   # Clone the source repository as mirror
  git filter-repo --path <directory_to_split> --path-rename <old_path>:<new_path>
  git push --mirror <new_repo_URL>   # Push the new repository
  ```

- Check and optimize Git hooks:
  Review and optimize custom Git hooks in the `.git/hooks` directory.

Ensure efficient Git operations by following these steps.

4\. **Caching and Load Balancing**:

\- Implement caching mechanisms to reduce the load on your GitHub
Enterprise Server. Caching can help serve frequently accessed resources
faster.

\- Consider load balancing if you have multiple servers to distribute
user requests evenly and improve overall performance.

5\. **Logs and Monitoring**:

- Regularly review server and GitHub Enterprise logs to identify any patterns or issues causing the performance problems.

  - To review GitHub Enterprise logs:

    ```bash
    tail -f /var/log/github/github.log
    ```

  - For server logs (replace `/var/log/app.log` with the actual log file):

    ```bash
    tail -f /var/log/app.log
    ```

- Use monitoring tools to gain insights into resource usage and potential bottlenecks.

  - Popular monitoring tools include:
    - **Prometheus**: For resource and application monitoring.
    - **Grafana**: To visualize data from Prometheus.
    - **New Relic**: For application performance monitoring.
    - **Datadog**: For cloud infrastructure monitoring.
    - **Zabbix**: For network and server monitoring.

Choose a monitoring tool that best fits your needs and integrate it with your infrastructure for effective resource management.

6\. **GitHub Enterprise Updates**:

- Ensure that your GitHub Enterprise Server is up to date with the latest patches and updates. Updates often include performance improvements and bug fixes.

To update your GitHub Enterprise Server, follow these commands:

1. Check for available updates.This utility will check to see if a new patch release of GitHub Enterprise is available. If it is, and if space is available on your instance, it will download the package. By default, it's saved to /var/lib/ghe-updates:

```bash
ghe-update-check
```

2. To install an upgrade package::

```bash
ghe-upgrade UPGRADE-PACKAGE-FILENAME
```

If you require further assistance or have specific questions about any
of these recommendations, please feel free to reach out.

Best regards,

Philip Badu

GitHub Enterprise Support Team

## Question 3

You receive a ticket from ACME, Inc. asking if it's possible to adjust GitHub Enterprise's web interface to match their corporate identity better.

> Hi, At ACME, Inc. we have many services running in-house, all matching our orange colored corporate design and showing the ACME, Inc. logo. GitHub Enterprise is the only service that does not seem to support this. How can we alter GitHub Enterprise's design?

GitHub currently does not support modifications to GitHub Enterprise's web interface for two reasons:

- GitHub Enterprise was designed to match GitHub.com to preserve the familiarity many software developers around the world have already acquired on GitHub.com. Changing the GitHub user experience by altering its design could be too confusing for the people actually using our product.
- Changing GitHub Enterprise's design would only be a cosmetic change. It wouldn't have a huge impact on improving how people collaborate and work together as other features we could be working on. There are other items on our product's roadmap with a higher prioritization.

Taking these reasons into account, how would you respond to the customer using your own words?

### Question #3 response

Dear ACME, Inc.,

Thank you for contacting GitHub Enterprise Technical Support. 
My name is Philip Badu, and I am the Support Engineer assigned to your service request.

I understand that you have concerns regarding customizing the
appearance of GitHub Enterprise to match your corporate identity.

We understand that maintaining consistent branding across your services is important. 
However, we do not currently support direct changes to the visual design of 
GitHub Enterprise's web interface. There are a few key reasons for this:

1\. **Keeping Things Familiar:** GitHub Enterprise was intentionally
designed to closely resemble GitHub.com. This approach aims to provide a
familiar experience for the millions of developers who are already using
GitHub.com. Making significant design alterations could potentially
confuse users who rely on the platform\'s current look and feel.

2\. **Priority on Functionality:** Our main focus is on enhancing
the functionality and collaboration features of GitHub Enterprise to
make it a powerful tool for teams. While design customization is
important, we currently prioritize features that directly improve how
teams work together.

We genuinely appreciate your feedback and understand your desire for a
more tailored appearance. While we cannot offer design customization
within the GitHub Enterprise interface right now, please know that we
continuously evaluate customer requests. We are always exploring ways to
enhance the platform based on your needs and suggestions.

If you have specific requirements or feature requests that can help
GitHub Enterprise better meet your organization\'s needs, please feel
free to share them with us. We are committed to assisting you in any way
possible and ensuring that GitHub Enterprise remains a valuable part of
your development and collaboration toolkit.

Thank you for choosing GitHub Enterprise, and if you have more questions
or concerns, please do not hesitate to reach out. We are here to support
you.

Warm regards,

Philip Badu

GitHub Enterprise Support Team

### Question 4

You receive the following ticket from a customer:

> Hi!
>
> After installing the latest update this morning I noticed that my browsers are now throwing Invalid SSL Cert errors when attempting to access our instance.
>
> $ curl -I [https://github.acme.edu](https://github.acme.edu/) curl: (60) SSL certificate problem, verify that the CA cert is OK. Details: error:14090086:SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed More details here: [http://curl.haxx.se/docs/sslcerts.html](http://curl.haxx.se/docs/sslcerts.html)
>
> Not sure if anyone else has reported this or what I might be able to do to fix it. I've re-uploaded our key & cert file to no avail.

Notes

You do not have shell or web interface access to their GitHub Enterprise instance, so in your reply you'll need to have the customer do any troubleshooting steps and return the results.

### Question #4 response

Hello Team,

Thank you for contacting GitHub Enterprise Technical Support. 
My name is Philip Badu, and I am the Support Engineer assigned to your service request.

I understand the inconvenience you have encountered and sincerely
apologize for any disruption this may have caused. Rest assured, we are
committed to helping you resolve this matter promptly.

Looking at the verbatim, it appears that the error
message you received when trying to access \'https://github.acme.edu\'
is pointing to a potential SSL certificate validation issue.

To address this concern, I recommend performing the following steps to
resolve the issue:

1\. **Update Certificate Authority (CA):** The error you are encountering often indicates that your Certificate Authority (CA) bundle may be out-of-date. Updating your operating system typically includes updating the CA bundle and can resolve this problem.

To update the CA bundle on Linux (Debian/Ubuntu):

```bash
sudo apt-get update
sudo apt-get install --reinstall ca-certificates
```

To update the CA bundle on Linux (Red Hat/CentOS):

```bash
sudo yum update
sudo yum reinstall ca-certificates
```

To update the CA bundle on macOS using Homebrew:

```bash
brew update
brew upgrade openssl
```

For Windows, it's usually updated as part of Windows Update.

2\. **Use Curl with Caution:** If you trust the GitHub instance and
its certificate, you can use the -k or \--insecure option with curl to
bypass certificate verification. For example: \`curl -k
<https://github.acme.edu>\`. However, please be aware that this approach
is not recommended from a security standpoint.

3\. **Configure Git to Use System Certificate Store:** You can configure Git to utilize your system\'s certificate store, which can help resolve SSL certificate issues. On Windows, you can achieve this by running the following command: 

```powershell
git config --global http.sslBackend schannel
```

On Linux, you can use this command:

```bash
git config --global
http.sslCAPath /etc/ssl/certs
```

4\. **Add Self-Signed Certificate:** If your certificate is
self-signed, you can add it to your system or Git\'s trusted
certificates. You can obtain the certificate by running:

```bash
openssl s_client -showcerts -connect <https://github.acme.edu:443>

``` 

Save it to a file and import it using your system\'s tools or Git\'s configuration.

For more detailed guidance and troubleshooting information, you can
access our documentation on this topic by visiting
[troubleshooting-ssh/error-ssl-certificate-problem-verify-that-the-ca-cert-is-ok](https://docs.github.com/en/enterprise-cloud@latest/authentication/troubleshooting-ssh/error-ssl-certificate-problem-verify-that-the-ca-cert-is-ok).

Should you encounter any difficulties or have questions while reviewing
the documentation, please do not hesitate to reach out to me. I'm here
to provide any additional support and guidance you may need.

We sincerely appreciate your choice to rely on our support for your
technical requirements, and we are committed to assisting you further.

Warm regards,

Philip Badu

GitHub Enterprise Support Team

