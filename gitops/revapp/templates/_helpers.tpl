{{- define "helpers.list-env-vars"}}
{{- range $key, $val := .Values.config }}
- name: {{ $key }}
  valueFrom:
    configMapKeyRef:
      name: app-cfg
      key: {{ $key }}
{{- end }}
{{- end }}

{{- define "helpers.list-secret-vars"}}
{{- range $key, $val := .Values.secrets }}
- name: {{ $key }}
  valueFrom:
    secretKeyRef:
      name: {{ $.Values.general.appName }}
      key: {{ $val }}
{{- end }}
{{- end }}

