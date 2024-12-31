# CloudCraftWithFranck-Monitoring

CloudCraftWithFranck-Monitoring is a simple API backend designed to fetch real-time statistics from GitHub repositories and YouTube channels. This project is deployed and live at [CloudCraftWithFranck Monitoring](https://cloudcraftwithfranck-monitoring.onrender.com).

---

## Features

- **GitHub Repository Statistics**:
  - Fetches the number of stars, forks, and open issues from a specified GitHub repository.

- **YouTube Channel Statistics**:
  - Retrieves views, subscribers, and total videos from a YouTube channel.

---

## Endpoints

### Base URL
The base URL for the API is:

### Available Endpoints
1. **GitHub Stats**:
   - URL: `/github-stats`
   - Example: [https://cloudcraftwithfranck-monitoring.onrender.com/github-stats](https://cloudcraftwithfranck-monitoring.onrender.com/github-stats)
   - Returns:
     ```json
     {
       "stars": 0,
       "forks": 0,
       "issues": 0
     }
     ```

2. **YouTube Stats**:
   - URL: `/youtube-stats`
   - Example: [https://cloudcraftwithfranck-monitoring.onrender.com/youtube-stats](https://cloudcraftwithfranck-monitoring.onrender.com/youtube-stats)
   - Returns:
     ```json
     {
       "views": 1234,
       "subscribers": 567,
       "videos": 89
     }
     ```

---

## Deployment

This project is deployed on [Render](https://render.com) and can be accessed via the following URL:
[https://cloudcraftwithfranck-monitoring.onrender.com](https://cloudcraftwithfranck-monitoring.onrender.com)

---

## Future Enhancements

- Add more GitHub metrics (e.g., pull requests, commit history).
- Include additional YouTube analytics like watch time and top-performing videos.
- Create a frontend to visualize the data.

---
The project is ingrated in [Grafana](https://cloudcraftwithfranck.grafana.net/d/be8j7o2lkkum8f/cloudcraftwithfranck-statistics-dashboard?orgId=1&from=now-6h&to=now&timezone=browser) and shows statistics as under: 
![image](https://github.com/user-attachments/assets/1586cd98-fa77-4c2f-825b-9a0a284b2764)


## License

This project is licensed under the MIT License.
