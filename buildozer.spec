      - name: Force Clean SDK Tools Cache Conflict
        run: |
          ANDROID_HOME=$HOME/.buildozer/android/platform/android-sdk
          rm -rf $ANDROID_HOME/cmdline-tools
          rm -rf $ANDROID_HOME/tools
          
