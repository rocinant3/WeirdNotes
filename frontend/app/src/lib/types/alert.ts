type AlertLevelType = "success" | "info" | "warning" | "default";


type AlertType = {
  level: AlertLevelType;
  message: string
}

export type {AlertType, AlertLevelType}
