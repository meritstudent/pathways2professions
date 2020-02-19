// Tutorial: https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Offline_Service_workers

var cacheName = 'myapp-cache-0.2';
var appShellFiles = [
  '/static/img/backg.png',
  '/static/img/icon-menu-png-23.jpg',
  '/static/img/logo.png',
  '/static/img/map.svg',
  '/static/img/Pathways-Logo-White-1.png',
  '/static/icon/favicon-16x16.png',
  '/static/icon/favicon-32x32.png',
  '/static/icon/favicon-96x96.png',
  '/static/icon/favicon-192x192.png',
  '/static/css/main.css',
  '/static/js/script.js',
  '/static/install/script.js',
  '/static/install/service-worker.js',

  '/templates/about.html',
  '/templates/base.html',
  '/templates/index.html',
  '/templates/map.html',
  '/templates/organizations.html',
];

self.addEventListener('install', (e) => {
    console.log('[Service Worker] Install');
    e.waitUntil(
    caches.open(cacheName).then((cache) => {
          console.log('[Service Worker] Caching all: app shell and content');
      return cache.addAll(appShellFiles);
    })
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((r) => {
          console.log('[Service Worker] Fetching resource: '+e.request.url);
      return r || fetch(e.request).then((response) => {
                return caches.open(cacheName).then((cache) => {
          console.log('[Service Worker] Caching new resource: '+e.request.url);
          cache.put(e.request, response.clone());
          return response;
        });
      });
    })
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keyList) => {
          return Promise.all(keyList.map((key) => {
        if(cacheName.indexOf(key) === -1) {
          return caches.delete(key);
        }
      }));
    })
  );
});

// Install prompt https://developers.google.com/web/fundamentals/app-install-banners/#listen_for_beforeinstallprompt
self.addEventListener('beforeinstallprompt', (e) => {
  // Stash the event so it can be triggered later.
  deferredPrompt = e;
  // Update UI notify the user they can add to home screen
  showInstallPromotion();
});
